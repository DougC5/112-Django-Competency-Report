var movies = [];
var serverURL = 'http://127.0.0.1:8000';
let order = {
    total: 0,
    client_id: 42,
    items: []
}

function getCatalog(){
    $.ajax({
        type: "GET",
        url: serverURL + '/api/movies',
        //data: "data",
        //dataType: "dataType",
        success: function (res) {
            movies = res.objects;
            for (let i = 0; i < movies.length; i++){
                // can add filtering
                displayMovie(movies[i]);
            }
            console.log(movies);
        },
        error: function (error) {
            console.error("**error", error);
        }
    });
}

function displayMovie(movie) {
    let tbody = $("#tblCatalog > tbody");
   var tr =  `<tr>
    <th scope="col">${movie.id}</th>
    <th scope="col">${movie.title}</th>
    <th scope="col">${movie.release_year}</th>
    <th scope="col">${movie.price}</th>
    <th scope="col">${movie.stock}</th>
    <th scope="col"><button type="button" movie-id="${movie.id}" class="btn btn-primary btnAdd">Add to Cart</button></th>
  </tr>`;
  tbody.append(tr);
}

function addToCart(movie) {
    order.items.push(movie);
    order.total += movie.price;

    var rentMovie = {
        movie_id: movie.id,
        quantity: 1
    };
    
    var found = false;
    for (let i = 0; i < order.items.length; i++){
        var indexM = order.items[i];
        if(indexM.id == rentMovie.movie_id){
            indexM.id += 1;
            found = true;
        }
                
    }
    if(!found){
        order.items.push(rentMovie);
    }

    

    $("#txtNumberItems").val(order.items.length);
    $("#txtTotal").val(order.total.toFixed(2));

}

function saveOrder(){
    $.ajax({
        type: "POST",
        url: serverURL + "/api/orders/",
        data: JSON.stringify(order),
        contentType: "application/json",
        success: function (res) {
            console.log('im a jedi DEV', res);
        }
    });
}

function init(){
    console.log('order.js loaded');

    // get movie catalog
    getCatalog();

    $('#btnSave').click(saveOrder());

    // hook event for add button
    // $(".btnAdd").click(function(e){
    //     console.log('button clicked');
    //     console.log(e);
    //     let id = $(this).attr('movie-id');
    //     console.log(id);
    // });

    $('#tblCatalog').on('click', '.btnAdd', function(){
        console.log('button clicked');
        let id = $(this).attr('movie-id');
        
        //find movie with this id
        for (let i = 0; i < movies.length; i++){
            let m = movies[i];
            if(m.id == id){
                addToCart(m);
                console.log(order.items);
                break;
            }
        }
        console.log(id);
    });
}

window.onload = init;