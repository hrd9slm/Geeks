let changeEnough=(itemPrice, amountOfChange)=>{
    let amount =[0.25,0.10,0.05,0.01]
    sum=0
    for(let i =0;i<=3;i++){
        sum+=amount[i]*amountOfChange[i]
 
    }
    if (itemPrice>sum){ return false}
    else{ return true}
    
    
}
console.log(changeEnough(14.11, [2,100,0,0]) )
console.log(changeEnough(0.75, [0,0,20,5]))