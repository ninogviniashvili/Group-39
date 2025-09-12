    const images = [
      "https://picsum.photos/id/1015/600/400",
      "https://picsum.photos/id/1025/600/400",
      "https://picsum.photos/id/1035/600/400",
      "https://picsum.photos/id/1045/600/400",
      "https://picsum.photos/id/1055/600/400"
    ];

    let currentIndex = 0;

    const slider = document.getElementById("slider");
    const prevBtn = document.getElementById("prevBtn");
    const nextBtn = document.getElementById("nextBtn");

    slider.src = images[currentIndex];

    nextBtn.addEventListener("click", () => {
      currentIndex++;
      if (currentIndex >= images.length) {
        currentIndex = 0; 
      }
      slider.src = images[currentIndex];
    });


    prevBtn.addEventListener("click", () => {
      currentIndex--;
      if (currentIndex < 0) {
        currentIndex = images.length - 1;
      }
      slider.src = images[currentIndex];
    });