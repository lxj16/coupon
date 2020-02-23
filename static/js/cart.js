// js for cart
// when user select add cart, add current coupon to local storage
$(document).ready(function() {
  updateShoppingCart();
  addToShoppingCartHandler();

  // $(document).on("keyup", "table input", handleCheckoutTable);
});

// todo: after refresh , same coupono can be selected again, change quantity

// helper function, get item from local storage and return as either {} or json format
function _renderLocalStorageAsJson(localstorage_key) {
  let data = window.localStorage.getItem(localstorage_key);
  if (data) {
    data_json = JSON.parse(data);
    return data_json;
  }
  return {};
}

// restore the number to #cart-num
function updateShoppingCart() {
  // window.localStorage.setItem("user", JSON.stringify(person));
  // window.localStorage.getItem('user');

  let shoppingCart = _renderLocalStorageAsJson("GSC-coupons");
  if (shoppingCart.length) {
    $("#cart-num").html(shoppingCart.length);
  }
}

function addToShoppingCartHandler() {
  $(".add-to-cart-btn").click(function() {
    $(this).html("added");
    $(this).removeClass("add-to-cart-btn");

    // get coupon id
    const couponCode = $(this).attr("data-code");

    let shoppingCart = _renderLocalStorageAsJson("GSC-coupons");
    console.log("test", shoppingCart);
    if (shoppingCart.length) {
      // not empty, append to local storage
      shoppingCart.push({ code: couponCode });
      window.localStorage.setItem("GSC-coupons", JSON.stringify(shoppingCart));
    } else {
      window.localStorage.setItem("GSC-coupons", JSON.stringify([{ code: couponCode }]));
      // empty, write to shopping cart
    }
    // update shopping cart
    updateShoppingCart();
  });
}