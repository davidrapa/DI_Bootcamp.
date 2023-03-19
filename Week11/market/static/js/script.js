// retrieve all products
fetch('/get_products')
  .then(response => response.json())
  .then(products => {
    // loop through each product and create HTML for it
    let productsHTML = ''
    products.forEach(product => {
      productsHTML += `
        <div class="product-card">
          <div class="product-image">
            <img src="${product.ProductPicUrl}">
          </div>
          <div class="product-info">
            <h3>${product.Name}</h3>
            <p class="description">${product.Description}</p>
            <p class="price">${product.Price} ${product.CurrencyCode}</p>
            <button class="add-to-cart-btn" data-product-id="${product.ProductId}">Add to Cart</button>
          </div>
        </div>
      `
    })

    // insert the products HTML into the DOM
    document.getElementById('products-container').innerHTML = productsHTML

    // add event listeners for the "add to cart" buttons
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn')
    addToCartButtons.forEach(button => {
      button.addEventListener('click', () => {
        const productId = button.getAttribute('data-product-id')
        fetch(`/add_to_cart/${productId}`)
          .then(response => response.json())
          .then(cartItems => {
            // update the cart count in the navbar
            document.getElementById('cart-count').innerHTML = cartItems.length
          })
      })
    })
  })

// retrieve cart items and display them
fetch('/get_cart_items')
  .then(response => response.json())
  .then(cartItems => {
    // loop through each cart item and create HTML for it
    let cartItemsHTML = ''
    let totalPrice = 0
    cartItems.forEach(cartItem => {
      totalPrice += cartItem.Price
      cartItemsHTML += `
        <div class="cart-item">
          <img src="${cartItem.ProductPicUrl}" class="cart-item-image">
          <div class="cart-item-info">
            <h3>${cartItem.Name}</h3>
            <p class="price">${cartItem.Price} ${cartItem.CurrencyCode}</p>
            <button class="delete-from-cart-btn" data-product-id="${cartItem.ProductId}">Remove from Cart</button>
          </div>
        </div>
      `
    })

    // insert the cart items HTML into the DOM
    document.getElementById('cart-items-container').innerHTML = cartItemsHTML

    // update the total price
    document.getElementById('total-price').innerHTML = `${totalPrice} EUR`

    // add event listeners for the "remove from cart" buttons
    const deleteFromCartButtons = document.querySelectorAll('.delete-from-cart-btn')
    deleteFromCartButtons.forEach(button => {
      button.addEventListener('click', () => {
        const productId = button.getAttribute('data-product-id')
        fetch(`/remove_from_cart/${productId}`)
          .then(response => response.json())
          .then(cartItems => {
            // update the cart count in the navbar
            document.getElementById('cart-count').innerHTML = cartItems.length
            // update the cart items in the DOM
            let updatedCartItemsHTML = ''
            let updatedTotalPrice = 0
            cartItems.forEach(cartItem => {
              updatedTotalPrice += cartItem.Price
              updatedCartItemsHTML += `
                <div class="cart-item">
                  <img src="${cartItem.ProductPicUrl}" class="cart-item
