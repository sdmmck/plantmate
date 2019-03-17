let plant;

function onload() {
    getPlant();
}

function getPlant() {

    let n = window.location.search.lastIndexOf("?");
    let result = window.location.search.substring(n + 1);
    let results = result.split("&");

    for (let r = 0; r < results.length; r++) {
        results[r] = results[r].split("=")[1];
        results[r] = results[r].replace("%2F", "/");
        results[r] = results[r].replace(/_/g, " ");
    }

    let plants = [allplants.length];
    for (let i = 0; i < allplants.length; i++) {
        plants[i] = 0;
    }

    for (let i = 0; i < allplants.length; i++) {
        if (results[0].toLowerCase() === allplants[i].size.toLowerCase()) {
            plants[i]++;
        }
        if (results[1].toLowerCase() === allplants[i].characteristics.toLowerCase()) {
            plants[i]++;
        }
        if (results[2].toLowerCase() === allplants[i].room.toLowerCase()) {
            plants[i]++;
        }
        if (results[3].toLowerCase() === allplants[i].climate.toLowerCase()) {
            plants[i]++;
        }
        if (results[4].toLowerCase() === allplants[i].light.toLowerCase()) {
            plants[i]++;
        }
        if (results[5].toLowerCase() === allplants[i].pet.toLowerCase()) {
            plants[i]++;
        }
    }

    let highestNumber = 0;
    let index = 0;
    for (let i = 0; i < allplants.length; i++) {
        console.log('index number = ' + i + ' index value =' + plants[i] + ' plant = ' + allplants[i].name);
        if (plants[i] > highestNumber) {
            index = i;
            highestNumber = plants[i];
        }
    }

    plant = allplants[index];
    updateDoc();
}

function updateDoc() {

    document.getElementById("match").innerHTML = "You've been matched with . . . " + plant.name;
    document.getElementById("description").innerText = plant.description;
    document.getElementById("size").innerText = "Size: " + plant.size;
    document.getElementById("characteristics").innerText = "Special characteristic: " + plant.characteristics;
    document.getElementById("room").innerText = "Room: " + plant.room;
    document.getElementById("climate").innerText = "Climate: " + plant.climate;
    document.getElementById("light").innerText = "Light: " + plant.light;
    document.getElementById("pet").innerText = "Suitable for pets: " + plant.pet;
    document.getElementById("wishlist_plant").value = plant.slug;
    document.getElementById("saved_plant").value = plant.slug;

    updateDocInline();

}
