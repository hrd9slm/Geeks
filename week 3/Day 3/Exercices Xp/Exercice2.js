const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  
const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 
const shoppingList =["banana","orange","apple"]
 let myBill=()=>{
    let sum=0
    for (let item of shoppingList) {
        if (stock[item]>=1){
        
            sum+=prices[item]
            stock[item]-=1
            console.log(`${item} dans le stock :${stock[item]}`)
        }
        else{
            console.log(`${item} pas dans le stock`)
        }
    }
    return sum


 }
 console.log(myBill())