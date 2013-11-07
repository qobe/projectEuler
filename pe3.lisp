(defun reload () (load "pe3.lisp"))

;;pe3
;;largest prime factor of 600851475143
(defun is-prime? (n)
  (setf prime? nil)
  (if (= 0 (mod n 2)) return prime?)
  (loop with i=3 do
       (cond ((= n i)
	      (= 0 (mod n i)) return prime?))
       (incf i 2)
       until (> i n))) 