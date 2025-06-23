let cuerpo=document.getElementsByClassName("fondo")[0];

fetch("/verifica/")
.then( response=> response.json())
.then((data) => {
    console.log(data, data.res, "aver");
    if (data.res=="True") {
    sesion_close()
    }
})

function opaco() {
    cuerpo.style.opacity="0.5"; 
    cuerpo.style.pointerEvents="none"
    cuerpo.style.backgroundColor="rgba(2, 18, 169, 0.3)"
}

function login() {
    let acceder=document.getElementsByClassName("login")[0]
    acceder.style.display="flex";
    acceder.style.opacity="0";
    acceder.style.transition="opacity 0.2s"
    setTimeout( () => { acceder.style.opacity="1"},0)
    opaco();
} 
c=0
let csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute("content");

function sesion_close() {
    document.getElementsByClassName("barra__acceder")[0].innerHTML="CERRAR"
    document.getElementsByClassName("barra__acceder")[0].style.backgroundColor="brown"
    document.getElementsByClassName("barra__acceder")[0].style.borderRadius="50%"
    let cerrar=document.getElementsByClassName("barra__acceder")[0]
    cerrar.addEventListener("click", function (a) {
        document.getElementsByClassName("login")[0].style.display="none";
        fetch("/cerrar/")
        .then(
            () => {
                window.location.reload()
            })
    })
}

document.getElementById("formulario_identificador").addEventListener("submit", function(event){
    event.preventDefault();

    let formulario_datos= {
        correo: this.elements["correo"].value,
        contraseña: this.elements["contraseña"].value
    };
    fetch("/procesar/", { 
        method: "POST",
        headers: {
            "Content-Type": "application/json", 
            "X-CSRFToken": csrfToken 
        },
        body: JSON.stringify(formulario_datos)
    })    
    .then(response => response.json())
    .then(data => {
        console.log(data,"amigooo");
        if (data.success) {
            document.getElementsByClassName("login")[0].style.display="none";
            document.getElementsByClassName("fondo")[0].style.pointerEvents="auto";
            document.getElementsByClassName("fondo")[0].style.opacity="1";
            sesion_close()
        };
    })
})

function cerrar_formu() {
    let cuerpo=document.getElementsByClassName("fondo")[0];
    document.getElementsByClassName("login")[0].style.display="none";
    cuerpo.style.pointerEvents="auto";
    cuerpo.style.opacity="1";
    cuerpo.style.backgroundColor="transparent"
}

let reg=document.getElementsByClassName("register")[0];


function cerrar_re() {
    reg.style.opacity="0"
    setTimeout(()=> {reg.style.display="none"},100);
    cuerpo.style.opacity="1";
    cuerpo.style.backgroundColor="transparent";
    cuerpo.style.pointerEvents="auto"
}

function registrar() {
    opaco();
    reg.style.display="flex";
    setTimeout( () => { reg.style.opacity="1"},0)
}

document.getElementById("formu_id").addEventListener("submit", function (event) {
    event.preventDefault();
    con=this.elements["contrasena_re"].value ;
    con_veri=this.elements["contra_ve_re"].value;
    if (con==con_veri) {
        let dato_reg={
        correo:this.elements["correo_re"].value,
        contraseña:con,
        contra_veri:con_veri
        }
        
        fetch("/registra/", {
            method:"POST",
            headers: {
                "Content-Type":"application/json",
                "X-CSRFToken":csrfToken
            },
            body: JSON.stringify(dato_reg)
        })
        .then(() => {
                cerrar_re();
                sesion_close()
            }
        )

    }
})




    /*
    fetch("/registrar/", {
        method:"POST",
        headers:{
            "Content-Type":"application/json",
            "X-CSRFToken":csrfToken
        },
        body:JSON.stringify(dataReg)
    })
    */





/*
    elemento=document.getElementsByClassName("formulario__correo")[0];
    elemento.addEventListener("focus", () => {
    const estilos = window.getComputedStyle(elemento);
    console.log(estilos.outline); // Muestra el contorno por defecto
})

*/