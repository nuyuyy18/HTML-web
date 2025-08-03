const d = new Date();
alert(`sekarang hari ${d}`)
alert("annyeong haseyo");

document.addEventListener("click", kotak);
function kotak () {
    const center = document.querySelector('#center');
    const konten = document.querySelector('#konten');
    
    konten.addEventListener("click", function() {
    if (konten){
        konten.textContent = "Hi Guys I'm Nuyuy";
    } else{
        konten.textContent = "Alloww"
    }
    

    });
    console.log('#center');

} 
