function buttons() {

    showPlant();
}


function showPlant() {

    let n = window.location.search.lastIndexOf("?");
    let result = window.location.search.substring(n + 1);
    let results = result.split("&");

    for (let r = 0; r < results.length; r++) {
        results[r] = results[r].split("=")[1];
        results[r] = results[r].replace("%2F", "/");
        results[r] = results[r].replace(/_/g, " ");
    }

    document.getElementById("results").innerText = results.toString();

    let plants = [allplants.length];
    let plant;

    for (let i = 0; i < allplants.length; i++) {
        plants[i] = 0;
    }

    console.log(allplants);

    for (let i = 0; i < allplants.length; i++) {

        if (results[0].toLowerCase() === allplants[i].size.toLowerCase()) {
            plants[i]++;
            console.log(allplants[i].name);
        }
        if (results[1].toLowerCase() === allplants[i].characteristics.toLowerCase()) {
            plants[i]++;
            console.log(allplants[i].name);
        }
        if (results[2].toLowerCase() === allplants[i].room.toLowerCase()) {
            plants[i]++;
            console.log(allplants[i].name);
        }
        if (results[3].toLowerCase() === allplants[i].climate.toLowerCase()) {
            plants[i]++;
            console.log(allplants[i].name);
        }
        if (results[4].toLowerCase() === allplants[i].light.toLowerCase()) {
            plants[i]++;
            console.log(allplants[i].name);
        }
        if (results[5].toLowerCase() === allplants[i].pet.toLowerCase()) {
            plants[i]++;
            console.log(allplants[i].name);
        }
    }


    let highestNumber = 0;
    let index = 0;
    for (let i = 0; i < allplants.length; i++) {
        console.log('index number = '+i+' index value =' + plants[i]+' plant = '+allplants[i].name);
        if (plants[i] > highestNumber) {
            index = i;
            highestNumber = plants[i];
        }
    }

    plant = allplants[index];

    document.getElementById("hi").innerHTML = plant.name;
    document.getElementById("quiz_results").style.display="none";

//


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