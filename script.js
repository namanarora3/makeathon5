
fetch("download.json")

.then(function(response){
   return response.json();
})
.then(function(products){
    
   let placeholder = document.querySelector("#data-output");
   let out = ""; 
   for(let product of products){
      out += `
         <tr>
            <td>${product.name}</td>
            <td>${product.category}</td>
            <td> <img src='${product.image}'> </td>
            <td>${product.location}</td>
            <td>${product.created}</td>
            <td>${product.completed}</td>
            <td>${product.approved}</td>
            <td>${product.assigned}</td>
         </tr>
      `;
   }
 
   placeholder.innerHTML = out;
});