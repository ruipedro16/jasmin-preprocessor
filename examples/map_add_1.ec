require import AllCore IntDiv CoreMap List Distr.
from Jasmin require import JModel_x86.
import SLH64.


require import Array4.
require import WArray4.



module M = {
  proc add_1 (x:W8.t) : W8.t = {
    
    
    
    x <- (x + (W8.of_int 1));
    return (x);
  }
  
  proc map_add_1_4 (a:W8.t Array4.t) : W8.t Array4.t = {
    var aux: int;
    
    var i:int;
    var t:W8.t;
    
    i <- 0;
    while (i < 4) {
      t <- a.[i];
      t <@ add_1 (t);
      a.[i] <- t;
      i <- i + 1;
    }
    return (a);
  }
}.

