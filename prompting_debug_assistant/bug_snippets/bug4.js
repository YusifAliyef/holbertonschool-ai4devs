function addDiscount(price, discount) {
    // Bug: string concatenation instead of numeric subtraction if types mismatch
    return price - discount;
}
