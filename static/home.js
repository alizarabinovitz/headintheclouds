function submitSearch(){
    console.log("hello")
    let search_term = $("#search_entry").val().trim()
    console.log("Searchedfor", search_term)
    let length = search_term.length
    if(length > 0){
        search_term_newpg(search_term)
    }
}

function search_term_newpg(search_term){
    window.location.replace("/search/" + search_term)
}

$(document).ready(function(){
    $("#example_block").empty()

    $( "#target" ).submit(function( event ) {
        event.preventDefault();
      });

    $("#submit_button").click(function(){
        submitSearch();
    })
})