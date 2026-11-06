function calculateTotalPrice(cartItems) {
    let total = 0;
    // Bug: using assignment '=' instead of comparison or incorrect iteration
    for (let i = 0; i <= cartItems.length; i++) {
        total += cartItems[i].price;
    }
    return total;
}
