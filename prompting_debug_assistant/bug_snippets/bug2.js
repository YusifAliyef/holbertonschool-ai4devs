function calculateTotalPrice(cartItems) {
    /**
     * Calculates total price of items in the cart.
     * Contains a logical error in the loop boundary.
     */
    let total = 0;
    // Intentional bug: <= instead of <
    for (let i = 0; i <= cartItems.length; i++) {
        if (cartItems[i] !== undefined && cartItems[i] !== null) {
            total += cartItems[i].price;
        }
    }
    return total;
}
