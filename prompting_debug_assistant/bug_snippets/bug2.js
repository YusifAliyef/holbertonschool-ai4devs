function calculateTotalPrice(cartItems) {
    let total = 0;
    // Logical error with boundary condition
    for (let i = 0; i <= cartItems.length; i++) {
        if (cartItems[i]) {
            total += cartItems[i].price;
        }
    }
    return total;
}
