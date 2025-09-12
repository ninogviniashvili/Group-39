// 1. push() – ელემენტის დამატება მასივის ბოლოში
let arr1 = [1, 2, 3];
arr1.push(4);
console.log(arr1); // [1, 2, 3, 4]

// 2. pop() – ბოლო ელემენტის წაშლა და დაბრუნება
let arr2 = [1, 2, 3];
let last = arr2.pop();
console.log(last); // 3
console.log(arr2); // [1, 2]

// 3. unshift() – ელემენტის დამატება მასივის დასაწყისში
let arr3 = [2, 3];
arr3.unshift(1);
console.log(arr3); // [1, 2, 3]

// 4. shift() – პირველი ელემენტის წაშლა და დაბრუნება
let arr4 = [1, 2, 3];
let first = arr4.shift();
console.log(first); // 1
console.log(arr4); // [2, 3]

// 5. slice(start, end) – ახალი მასივი start–დან end–ამდე (end არ შედის), ორიგინალი არ იცვლება
let arr5 = [1, 2, 3, 4, 5];
let part = arr5.slice(1, 4);
console.log(part); // [2, 3, 4]
console.log(arr5); // [1, 2, 3, 4, 5]

// 6. splice(start, deleteCount, item1, ...) – ამოჭრის ელემენტები, ასევე შეუძლია ახალი ელემენტების დამატება, ორიგინალი იცვლება
let arr6 = [1, 2, 3, 4];
arr6.splice(1, 2, "a", "b"); // 1–დან 2 ელემენტის წაშლა და ჩანაცვლება "a", "b"-თ
console.log(arr6); // [1, "a", "b", 4]
