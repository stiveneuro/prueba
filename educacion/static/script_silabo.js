const barra_tema=document.getElementsByClassName("barra__tema")[0];
const capitulo__texto=document.getElementsByClassName("capitulo__texto")[0];
const modulo_texto=document.getElementsByClassName("modulo__texto")[0];
/* segun lo que reciba */

let csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute("content");

function click_mod(a) {
    a.classList.add("sele_conte");
    console.log(a.id,"mi amifo");
    id_modulo={"id_mod": a.id};
    fetch("modulos/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken
        },
        credentials: "include",
        body: JSON.stringify(id_modulo),
    })
    .then(response=> response.json())
    .then(data => {
        console.log(data);
        modulo_texto.style.transition="none";
        modulo_texto.style.opacity="0";
        setTimeout(() => {
            modulo_texto.innerHTML=data.modulo;
            modulo_texto.style.transition="opacity 1s";
            modulo_texto.style.opacity="1"
        },10)
    })
}

function modulo_vista() {
    contenido_capitulo=Array.from(document.getElementsByClassName("texto__contenido"));
    console.log(contenido_capitulo[0],"amigo mio");
    contenido_capitulo.forEach(a => { 
        a.addEventListener("mouseover", function(event) {
            console.log("comida comida")

            ob=capitulo__texto.getElementsByClassName("sele_conte")[0];
            console.log(ob,"comida amigod sino come");

            if (Boolean(ob)) {
                if (a.id!=ob.id) {
                    ob.classList.remove("sele_conte");
                    click_mod(a);
                }
            } else {
                click_mod(a)
            }
            
        })
    })
}

function cap_click(a) {
            a.classList.add("sele_circu")
            console.log(a.id);
            id_cap={"id_cap": parseInt(a.id)};
            console.log(id_cap,"dino");
            fetch("capcon/", {
                method: "POST",
                headers: {
                    "Content-Type":"application/json",
                    "X-CSRFToken":csrfToken
                },
                credentials: "include",
                body: JSON.stringify(id_cap)
            })
            .then(response => response.json())
            .then(data => {
                c=0;
                capitulo__texto.innerHTML=data.con_cap;
                console.log("desarrolla");
                elementos=capitulo__texto.querySelectorAll("li");
                elementos.forEach(e => {
                    contenido=e.innerHTML;
                    e.innerHTML=`<a href="" class='texto__prueba' ></a><a id="${data.id_mod[c]}" href="" class='texto__contenido' >${contenido}</a>`;
                    c+=1
                });

                modulo_vista();
            });
}

function cap_con() {
    capitulos=Array.from(barra_tema.getElementsByTagName("li"));
    capitulos.forEach(a => {
        a.addEventListener("click", function (event) {
            selecircu=barra_tema.getElementsByClassName("sele_circu")[0]
            if (Boolean(selecircu)) {
                if (a.id!=selecircu.id) {
                    selecircu.classList.remove("sele_circu");
                    cap_click(a);
                }
            } else {
                cap_click(a);
            }
            console.log("hola");
        })
    });
    capitulos[0].click();
    console.log(capitulos);
}



function capitulos(){
    fetch("capitulos/")
        .then(response => { console.log(response);return response.json()})
        .then( data => {
            data=data.lis_cap;
            console.log(data,"gola");
            data.forEach(element => {
                barra_tema.innerHTML+=`<li id="${element[0]}"><div class="tema__circuloG" style="background-color:${element[2] ?? '' }"><div class="circuloG__circuloP">${ element[1] ?? '0%'}</div></div></li>`;       
            });
            cap_con();
        })
}

capitulos();
/* Editamos los li del contenedor */





/*




*/
