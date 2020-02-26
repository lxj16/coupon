function handleCheckoutTable() {
  // NOTE: for now, coupon purchase price is 50% of the face value, we hard code this for now,
  // may need to make this value dynamic in the furture
  const pricePretentage = 0.5;
  let total = 0;

  $('.checkout_tr').each(function() {
    const discount = $(this).attr('data-discount');
    // total amount to purchase:
    let checkout_purchase = $(this)
      .find('input.checkout_purchase')
      .val();
    //update coupon value
    const conupon_value = (checkout_purchase * discount/100).toFixed(2);

    $(this)
      .find('.checkout_coupon_value')
      .html(conupon_value);
    // update price
    const price = (conupon_value * pricePretentage).toFixed(2);
    $(this)
      .find('.checkout_price')
      .html(conupon_value);

    // get amount
    let amount = $(this)
      .find('input.checkout_amount')
      .val();

    //update subtotal
    const subtotal = (amount * price).toFixed(2);
    $(this)
      .find('.checkout_subtotal')
      .html(subtotal);

    //calculate total
    total += +subtotal;
  });
  // update total
  $('#checkout_total').html(total.toFixed(2));
}

// helper function, get item from local storage and return as either {} or json format
function _renderLocalStorageAsJson(localstorage_key) {
  let data = window.localStorage.getItem(localstorage_key);
  if (data) {
    data_json = JSON.parse(data);
    return data_json;
  }
  return {};
}

const renderCart = () => {
  const cart = _renderLocalStorageAsJson('GSC-coupons');
  const items = cart.map(
    item => `
    <tr class="checkout_tr" data-discount="${item.couponDiscount}">
      <td class="checkout_name">${item.couponName}</td>
      <td><input type="number" value="100" class="checkout_purchase" /></td>
      <td class="checkout_coupon_value">some value</td>
      <td class="checkout_price">some value</td>
      <td><input type="number" value="1" class="checkout_amount"></td>
    <td class="checkout_subtotal">some value</td>
 </tr>
    `
  );

  $('#checkout_table_body').append(items);
};

function purchase() {
  $('#buyBtn').click(function(){
    console.log('clicked')
  })
}

// js for checkout handler
$(document).ready(function() {
  console.log('cartss');
  renderCart();
  handleCheckoutTable();
  purchase();
  // on change handler
  $(document).on('keyup', 'table input', handleCheckoutTable);
});
