
function manualMap(arr, callback) {
    const result = [];
    for(let i = 0; i < arr.length; i++){
        result.push(callback(arr[i], i, arr));
    }
    return result;
}

let nums = [1,2,3];
console.log(manualMap(nums, x => x * 2)); // [2,4,6]
console.log(manualMap(nums, x => x + 5)); // [6,7,8]
console.log(manualMap(nums, (x,i) => x + i)); // [1,3,5]





function manualFilter(arr, callback) {
    const result = [];
    for(let i = 0; i < arr.length; i++){
        if(callback(arr[i], i, arr)){
            result.push(arr[i]);
        }
    }
    return result;
}

console.log(manualFilter(nums, x => x > 1)); // [2,3]
console.log(manualFilter(nums, x => x % 2 === 0)); // [2]
console.log(manualFilter(nums, (x,i) => i % 2 === 0)); // [1,3]
