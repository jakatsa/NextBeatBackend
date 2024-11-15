from django.db import models
from users.models import User
from beats.models import Beat, License

# Order Model: Represents an order placed by a user.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    beats = models.ManyToManyField(Beat, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order by {self.user.username} - {self.created_at.strftime('%Y-%m-%d')}"

# Tax Model: Represents different tax rates.
class Tax(models.Model):
    name = models.CharField(max_length=50)  # Name of the tax (e.g., VAT, Sales Tax)
    rate = models.DecimalField(max_digits=5, decimal_places=2)  # Tax rate in percentage
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp of last update

    def __str__(self):
        return f"{self.name}: {self.rate}%"

# OrderItem Model: Represents each item in the order.
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    beat = models.ForeignKey(Beat, on_delete=models.CASCADE)
    license = models.ForeignKey(License, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True)  # Link to Tax model
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False,default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Calculate subtotal and total price
        self.subtotal = self.price_at_purchase * self.quantity
        # Apply tax if applicable
        tax_amount = (self.tax.rate / 100) * self.subtotal if self.tax else 0
        self.total_price = self.subtotal - self.discount + tax_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.beat.title} ({self.license.type})"

# Cart Model: Represents a user's shopping cart.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beat = models.ManyToManyField(Beat, through='CartItem')
    session_key = models.CharField(max_length=40, null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart for {self.user.username} - {self.created_at.strftime('%Y-%m-%d')}"

    def get_cart_total(self):
        """Calculate the total cost of all items in the cart."""
        total = sum(item.get_total_price() for item in self.cart_items.all())  # Updated 'items' to 'cart_items'
        return total

    def get_total_items(self):
        """Calculate the total quantity of items in the cart."""
        return sum(item.quantity for item in self.cart_items.all())  # Updated 'items' to 'cart_items'

# CartItem Model: Represents each item in the cart.
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')  # Updated related name
    beat = models.ForeignKey(Beat, on_delete=models.CASCADE)
    license = models.ForeignKey(License, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensure unique combination of cart and beat
        unique_together = ('cart', 'beat')

    def __str__(self):
        return f"{self.quantity} x {self.beat.title} ({self.license.type}) in cart"

    def get_total_price(self):
        """Calculate the total price for the cart item based on quantity."""
        return self.quantity * self.price

# Payment Model: Represents a payment made for an order.
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    payment_method = models.CharField(max_length=50, choices=[
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('Mpesa', 'Mpesa'),
        ('bank_transfer', 'Bank Transfer'),
    ])
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ], default='pending')

    def __str__(self):
        return f"Payment of {self.total_price} for Order {self.order.id} via {self.payment_method}"
