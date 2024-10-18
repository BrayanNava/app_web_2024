function operaciones(){
    let n1,n2,tipoope,ope,respuesta;

    n1 = parseInt(document.getElementById("n1").value);
    n2 = parseInt(document.getElementById("n2").value);
    valor = document.getElementById("select").value;

    if (isNumber(n1) && isNumber(n2)) 

        {
            switch(valor){
                case "+":
                    resultado = n1 + n2;
                    break;
                case "-":
                    resultado = n1 - n2;
                    break;
                case "*":
                    resultado = n1 * n2;
                    break;
                case "/":
                    resultado = n1 / n2;
                    break;
        }
        let respuesta = document.getElementById("resultado")
        respuesta.innerHTML=`<h2>${n1} ${valor} ${n2} = ${resultado}</h2>`;
    }

    else{
        respuesta = document.getElementById("resultado")
        respuesta.innerHTML=`<h2>Ingresa solo numeros por favor...</h2>`;
        alert('Ingresa solo numeros por favor...')
    }

}

function isNumber(n)
{
    return !isNaN(parseInt(n) && isFinite(n))
}