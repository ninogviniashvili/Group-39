const classObj = {
    studentCount: 25,
    grade: 7,
    favSubject: "Georgian"
}
  
if (classObj.studentCount > 30) {
    console.log("very big class");
  }
    else {
    console.log("Small Class");
}

if (classObj.grade >= 10) {
    console.log("High grade");
  } 
  else {
    console.log("Lower grade");
}
  
if (classObj.favSubject === "Georgian") {
    console.log("Georgian is the favorite subject");
} 
  else {
    console.log("Different favorite subject");
}