function addDiscount(price, discount) {
    /**
     * Subtracts discount from the given base price.
     * Potential type misuse if parameters are passed as strings.
     */
    let parsedPrice = parseFloat(price);
    let parsedDiscount = parseFloat(discount);
    
    if (isNaN(parsedPrice) || isNaN(parsedDiscount)) {
        return 0;
    }
    
    return parsedPrice - parsedDiscount;
}
