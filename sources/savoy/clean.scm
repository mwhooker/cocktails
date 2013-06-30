(define get-Type
  (lambda (x)
    (cond ((number? x) "Number")
          ((pair? x) "Pair")
          ((string? x) "String")
          ((list? x) "List")))) 


 (define (simple-antialias filename outname)
   (let* ((image (car (gimp-file-load RUN-NONINTERACTIVE filename filename)))
          (drawable (car (gimp-image-get-active-layer image))))
     (plug-in-sharpen RUN-NONINTERACTIVE image drawable 65)
     (let* ((threshold (get-auto-threshold (get-hist drawable 5))))
         (gimp-threshold drawable threshold 255)
         (gimp-message (number->string threshold))
     )
     (plug-in-antialias RUN-NONINTERACTIVE image drawable)
     (gimp-image-convert-indexed image 0 3 0 FALSE TRUE "")
;     (savoy-slice image drawable)
     (gimp-file-save RUN-NONINTERACTIVE image drawable outname outname)
     (gimp-image-delete image)))

(define (savoy-slice image drawable)
  (script-fu-guide-new-percent RUN-NONINTERACTIVE image drawable 2 50)
  (script-fu-guide-new-percent RUN-NONINTERACTIVE image drawable 1 50)
  (let* ((sliced-images (plug-in-guillotine RUN-NONINTERACTIVE image drawable)))
    (while 
    ;(map  (lambda (x) (gimp-message (number->string x))) (vector->list (cdr sliced-images)))
    ;(gimp-message (car (cdr sliced-images)))
    (gimp-message (number->string (car sliced-images)))))


; http://stackoverflow.com/a/8462738/105571
(define (auto-threshold imagePath)
  (let* (
         (theImage (car (gimp-file-load
                          RUN-NONINTERACTIVE
                          imagePath
                          imagePath)))
         (theDrawable (car  (gimp-image-get-active-drawable theImage)))
         (hist (get-hist theDrawable 0)))
    (get-auto-threshold hist)
    )
  )

;returns the threshold
(define (get-auto-threshold hist)
  (let*
    (
     (hist_max (vector-ref hist 0))
     (chist (make-vector 256))
     (cmom (make-vector 256))
     (maxval 255) ;end - start
     (i 1)
     (tmp )
     (chist_max)
     (cmom_max)
     (bvar_max 0)
     (threshold 127)
     )

    (vector-set! chist 0 (vector-ref hist 0))
    (vector-set! cmom 0 0)

    (set! i 1)
    (while (<= i maxval)
           (if (> (vector-ref hist i) hist_max)
             (set! hist_max (vector-ref hist i))
             )
           (vector-set! chist i (+ (vector-ref chist (- i 1)) (vector-ref hist i)) )
           (vector-set! cmom i (+ (vector-ref cmom (- i 1)) (* i (vector-ref hist i))) )
           (set! i (+ i 1))
           )

    (set! chist_max (vector-ref chist maxval))
    (set! cmom_max (vector-ref cmom maxval))

    (set! i 0)
    (while (< i maxval)
           (if (and (> (vector-ref chist i) 0) (< (vector-ref chist i) chist_max) )
             (let*
               ((bvar (/ (vector-ref cmom i) (vector-ref chist i))))

               (set! bvar (- bvar (/ (- cmom_max (vector-ref cmom i)) (- chist_max (vector-ref chist i)) ) ))
               (set! bvar (* bvar bvar))
               (set! bvar (* bvar (vector-ref chist i)) )
               (set! bvar (* bvar (- chist_max (vector-ref chist i)) ))

               (if (> bvar bvar_max)
                 (begin
                   (set! threshold i)
                   (set! bvar_max bvar)
                   )
                 )

               )
             )
           (set! i (+ i 1))
           )
    threshold
    )
  )

;returns the raw histogram  with values 0-1 as an array
(define (get-hist drawable chan)
  (let* (
         (i 0)
         (hist (make-vector 256))
         )
    (set! i 0)
    (while (< i 256)
           (vector-set! hist i (car (cddddr (gimp-histogram drawable chan i i))))
           (set! i (+ i 1))
           )
    hist
    )
  )
