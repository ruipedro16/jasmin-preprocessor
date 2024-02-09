require import AllCore IntDiv CoreMap List Distr.
from Jasmin require import JModel_x86.
import SLH64.





module M = {
  proc memcmp (p:W64.t, q:W64.t, n:W64.t) : W64.t = {
    
    var res_0:W64.t;
    var i:W64.t;
    var a:W64.t;
    var b:W64.t;
    
    res_0 <- (W64.of_int 1);
    i <- (W64.of_int 0);
    
    while ((i \ult n)) {
      a <- (loadW64 Glob.mem (W64.to_uint (p + (W64.of_int 0))));
      b <- (loadW64 Glob.mem (W64.to_uint (q + (W64.of_int 0))));
      if ((a <> b)) {
        res_0 <- (W64.of_int 0);
      } else {
        
      }
      p <- (p + (W64.of_int 4));
      q <- (q + (W64.of_int 4));
      i <- (i + (W64.of_int 1));
    }
    res_0 <- res_0;
    return (res_0);
  }
}.

