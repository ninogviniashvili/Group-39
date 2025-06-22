function Movie (name , genre, year, imbd, review){
    this.name=name
    this.genre=genre
    this.year=year
    this.imbd=imbd
    this.review=review

    this.film=function(){
        return `film: "${this.name}" year: ${this.year}, genre: ${this.genre}, IMDB: ${this.imdb}/10. review: ${this.review}`;
    }

}

const film1=new Movie("The godfather", 1972, "drama", 9.2, "good performance.")
console.log(film1.film());

