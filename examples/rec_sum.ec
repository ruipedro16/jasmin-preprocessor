require import AllCore IntDiv CoreMap List Distr.
from Jasmin require import JModel_x86.
import SLH64.


require import Array1 Array2 Array3 Array4 Array5 Array6 Array7 Array8 Array9
               Array10.
require import WArray8 WArray16 WArray24 WArray32 WArray40 WArray48 WArray56
               WArray64 WArray72 WArray80.



module M = {
  proc sum_array_1 (a:W64.t Array1.t, acc:W64.t) : W64.t = {
    
    var t:W64.t;
    
    t <- a.[0];
    acc <- acc;
    acc <- (acc + t);
    acc <- acc;
    return (acc);
  }
  
  proc sum_array_2 (a:W64.t Array2.t, acc:W64.t) : W64.t = {
    
    var sum_tail:W64.t;
    var tail:W64.t Array1.t;
    tail <- witness;
    sum_tail <- sum_tail;
    acc <- acc;
    tail <- (Array1.init (fun i => a.[1 + i]));
    sum_tail <@ sum_array_1 (tail, acc);
    sum_tail <- sum_tail;
    acc <- acc;
    acc <- (acc + sum_tail);
    return (acc);
  }
  
  proc sum_array_3 (a:W64.t Array3.t, acc:W64.t) : W64.t = {
    
    var sum_tail:W64.t;
    var tail:W64.t Array2.t;
    tail <- witness;
    sum_tail <- sum_tail;
    acc <- acc;
    tail <- (Array2.init (fun i => a.[1 + i]));
    sum_tail <@ sum_array_2 (tail, acc);
    sum_tail <- sum_tail;
    acc <- acc;
    acc <- (acc + sum_tail);
    return (acc);
  }
  
  proc sum_array_4 (a:W64.t Array4.t, acc:W64.t) : W64.t = {
    
    var sum_tail:W64.t;
    var tail:W64.t Array3.t;
    tail <- witness;
    sum_tail <- sum_tail;
    acc <- acc;
    tail <- (Array3.init (fun i => a.[1 + i]));
    sum_tail <@ sum_array_3 (tail, acc);
    sum_tail <- sum_tail;
    acc <- acc;
    acc <- (acc + sum_tail);
    return (acc);
  }
  
  proc sum_array_5 (a:W64.t Array5.t, acc:W64.t) : W64.t = {
    
    var sum_tail:W64.t;
    var tail:W64.t Array4.t;
    tail <- witness;
    sum_tail <- sum_tail;
    acc <- acc;
    tail <- (Array4.init (fun i => a.[1 + i]));
    sum_tail <@ sum_array_4 (tail, acc);
    sum_tail <- sum_tail;
    acc <- acc;
    acc <- (acc + sum_tail);
    return (acc);
  }
  
  proc sum_array_6 (a:W64.t Array6.t, acc:W64.t) : W64.t = {
    
    var sum_tail:W64.t;
    var tail:W64.t Array5.t;
    tail <- witness;
    sum_tail <- sum_tail;
    acc <- acc;
    tail <- (Array5.init (fun i => a.[1 + i]));
    sum_tail <@ sum_array_5 (tail, acc);
    sum_tail <- sum_tail;
    acc <- acc;
    acc <- (acc + sum_tail);
    return (acc);
  }
  
  proc sum_array_7 (a:W64.t Array7.t, acc:W64.t) : W64.t = {
    
    var sum_tail:W64.t;
    var tail:W64.t Array6.t;
    tail <- witness;
    sum_tail <- sum_tail;
    acc <- acc;
    tail <- (Array6.init (fun i => a.[1 + i]));
    sum_tail <@ sum_array_6 (tail, acc);
    sum_tail <- sum_tail;
    acc <- acc;
    acc <- (acc + sum_tail);
    return (acc);
  }
  
  proc sum_array_8 (a:W64.t Array8.t, acc:W64.t) : W64.t = {
    
    var sum_tail:W64.t;
    var tail:W64.t Array7.t;
    tail <- witness;
    sum_tail <- sum_tail;
    acc <- acc;
    tail <- (Array7.init (fun i => a.[1 + i]));
    sum_tail <@ sum_array_7 (tail, acc);
    sum_tail <- sum_tail;
    acc <- acc;
    acc <- (acc + sum_tail);
    return (acc);
  }
  
  proc sum_array_9 (a:W64.t Array9.t, acc:W64.t) : W64.t = {
    
    var sum_tail:W64.t;
    var tail:W64.t Array8.t;
    tail <- witness;
    sum_tail <- sum_tail;
    acc <- acc;
    tail <- (Array8.init (fun i => a.[1 + i]));
    sum_tail <@ sum_array_8 (tail, acc);
    sum_tail <- sum_tail;
    acc <- acc;
    acc <- (acc + sum_tail);
    return (acc);
  }
  
  proc sum_array_10 (a:W64.t Array10.t, acc:W64.t) : W64.t = {
    
    var sum_tail:W64.t;
    var tail:W64.t Array9.t;
    tail <- witness;
    sum_tail <- sum_tail;
    acc <- acc;
    tail <- (Array9.init (fun i => a.[1 + i]));
    sum_tail <@ sum_array_9 (tail, acc);
    sum_tail <- sum_tail;
    acc <- acc;
    acc <- (acc + sum_tail);
    return (acc);
  }
}.

