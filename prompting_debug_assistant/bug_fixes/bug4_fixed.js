function addDiscount(price, discount) {
    /**
     * Subtracts discount from the given base price safely.
     * Fixed by explicit numeric parsing using parseFloat.
     */
    let parsedPrice = parseFloat(price);
    let parsedDiscount = parseFloat(discount);
    
    if (isNaN(parsedPrice) || isNaN(parsedDiscount)) {
        return 0;
    }
    
    return parsedPrice - parsedDiscount;
}
