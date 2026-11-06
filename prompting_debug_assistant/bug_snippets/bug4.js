function addDiscount(price, discount) {
    // Data type misuse: string subtraction can yield NaN if not handled
    let parsedPrice = parseFloat(price);
    let parsedDiscount = parseFloat(discount);
    return parsedPrice - parsedDiscount;
}
