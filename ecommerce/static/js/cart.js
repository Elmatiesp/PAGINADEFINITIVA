var UpdateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < UpdateBtns.length; i++){
    UpdateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId', productId, 'action', action)

        console.log('USER', user)
        if(user === 'AnonymousUser'){
            addCookieItem(productId, action)
        }else{
            updateUserOrder(productId, action)
        }
    })
}

function addCookieItem(productId, action){
    console.log('No estas logged..')

    if(action == 'add'){
        if(cart[productId] == undefined){
            cart[productId] = {'quantity':1}
        }else{
            cart[productId]['quantity'] += 1
        }
    }

    if(action == 'remove'){
        cart[productId]['quantity'] -= 1

        if(cart[productId]['quantity'] <= 0){
            console.log('Remove item')
            delete cart[productId]
        }
    }
    console.log('Cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}

function updateUserOrder(productId, action){
    console.log('Usuario ingresado, enviando data')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'content-Types':'Application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action':action})
    })

    .then((Response) =>{
        return Response.json();
    })

    .then((data) =>{
        console.log('data:', data)
        location.reload();
    });

}