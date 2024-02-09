require import AllCore IntDiv CoreMap List Distr.
from Jasmin require import JModel_x86.
import SLH64.


require import Array3.
require import WArray3.



module M = {
  proc __memcpy_3_u8 (dest:W8.t Array3.t, src:W8.t Array3.t) : W8.t Array3.t = {
    var aux: int;
    
    var i:int;
    var t:W8.t;
    
    i <- 0;
    while (i < 3) {
      t <- src.[i];
      dest.[i] <- t;
      i <- i + 1;
    }
    return (dest);
  }
}.

