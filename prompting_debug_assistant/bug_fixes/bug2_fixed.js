function calculateTotalPrice(cartItems) {
    /**
     * Calculates total price of items in the cart.
     * Fixed loop condition from <= to <.
     */
    let total = 0;
    for (let i = 0; i < cartItems.length; i++) {
        if (cartItems[i] && typeof cartItems[i].price === 'number') {
            total += cartItems[i].price;
        }
    }
    return total;
}
