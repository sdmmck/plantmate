function buttons() {

    document.getElementById("hi").innerHTML = "IN YOUR FACE DJANGO I AM A FULLY FUNCTIONAL BUTTON";

    console.log(allplants);

    showPlant();

}


function showPlant() {

    let n = window.location.search.lastIndexOf("?");
    let result = window.location.search.substring(n + 1);
    let results = result.split("&");

    for(let r = 0; r<results.length; r++){
        results[r] = results[r].split("=")[1];
    }

    document.getElementById("results").innerText = results.toString();


//    things to do:
    /*
    - need to make sure the same tags are stored in the database and assigned to the html
    - need to iterate over the list of plants to find one that matches the tags selected in the quiz
    - need to make it so that it is obligatory to select a radio button / set a default for each one
    - need to store a variable that contains the plant slug in it in the java script once the correct plant is found
    - need to get the javascript to update empty image tags and links with the correct information
    - need to add links to page to allow users to save plant to wishlist or my plants
    - need to link up this sheet to original quiz page button and remove button from this page
     */


}