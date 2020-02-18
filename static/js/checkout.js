function handleCheckoutTable() {
  // NOTE: for now, coupon purchase price is 50% of the face value, we hard code this for now,
  // may need to make this value dynamic in the furture
  const pricePretentage = 0.5;
  let total = 0;

  $(".checkout_tr").each(function() {
    const discount = $(this).attr("data-discount");
    // total amount to purchase:
    let checkout_purchase = $(this)
      .find("input.checkout_purchase")
      .val();
    //update coupon value
    const conupon_value = (checkout_purchase * discount).toFixed(2);

    $(this)
      .find(".checkout_coupon_value")
      .html(conupon_value);
    // update price
    const price = (conupon_value * pricePretentage).toFixed(2);
    $(this)
      .find(".checkout_price")
      .html(conupon_value);

    // get amount
    let amount = $(this)
      .find("input.checkout_amount")
      .val();

    //update subtotal
    const subtotal = (amount * price).toFixed(2);
    $(this)
      .find(".checkout_subtotal")
      .html(subtotal);

    //calculate total
    total += +subtotal;
  });
  // update total
  $("#checkout_total").html(total.toFixed(2));
}

// js for checkout handler
$(document).ready(function() {
  handleCheckoutTable();

  // on change handler
  $(document).on("keyup", "table input", handleCheckoutTable);
});
