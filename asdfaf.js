function factorialize(num) {
    var total = 1;
    for (var i = 1; i < num + 1; i += 1) {
        total = (total * i);
    }
    return total
}

console.log(factorialize(5));