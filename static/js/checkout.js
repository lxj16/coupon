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
    const conupon_value = ((checkout_purchase * discount) / 100).toFixed(2);

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
  if (cart.length) {
    const items = cart.map(
      item => `
      <tr class="checkout_tr" data-discount="${item.couponDiscount}">
        <td class="checkout_name">${item.couponName}</td>
        <td><input type="number" value="100" class="checkout_purchase" min="0" id="${item.code}Estimate" /></td>
        <td class="checkout_coupon_value" id="${item.code}Value">some value</td>
        <td class="checkout_price">some value</td>
        <td><input type="number" id="${item.code}Quantity" value="1" class="checkout_amount" min="0" step="1"></td>
      <td class="checkout_subtotal" id="${item.code}Subtotal">some value</td>
   </tr>
      `
    );
  
    $('#checkout_table_body').append(items);
  }else{
    $('#checkout_table_body').append("<h2>Your cart is empty</h2>");
  }
};

function purchase() {
  $('#buyBtn').click(function() {
    const cart = _renderLocalStorageAsJson('GSC-coupons');
    const orderItems = [];
    cart.map(item => {
      const estimate = Number($(`#${item.code}Estimate`).val());
      const couponValue = Number($(`#${item.code}Value`).html());
      const quantity = Number($(`#${item.code}Quantity`).val());
      const subtotal = Number($(`#${item.code}Subtotal`).html());
      const orderItem = {
        code: item.code,
        estimate: estimate,
        couponValue: couponValue,
        quantity: quantity,
        subtotal: subtotal
      };
      orderItems.push(orderItem);
    });
    const sentToType = $("input[name='send_to']:checked").val();
    const sentTo =
      sentToType === 'phone'
        ? $("input[name='send_to_phone']").val()
        : $("input[name='send_to_email']").val();
    const order = {
      orderItems: orderItems,
      sentToType: sentToType,
      sentTo: sentTo
    };

    $.ajax({
      type: 'POST',
      url: '/coupon/checkout/',
      data: JSON.stringify(order),
      success: () => {
        console.log('success');
        localStorage.clear();
      }
    });
  });
}

// js for checkout handler
$(document).ready(function() {
  renderCart();
  handleCheckoutTable();
  purchase();
  // on change handler
  $(document).on('keyup', 'table input', handleCheckoutTable);
});
