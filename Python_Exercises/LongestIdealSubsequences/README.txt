DATA SEGMENT 
    num DB 0, 1, 2, 3, 4, 5, 6, 7, 8, 9    ; Array of decimal values 0-9,BİNARY VERSION OF THEM=HEX VERS 
    ones_count DB 10 DUP(?)                   ; Array to store counts of 1s
DATA ENDS

CODE SEGMENT
ASSUME CS:CODE, DS:DATA
START:
    MOV AX, DATA
    MOV DS, AX

    ; Initialize pointers
    MOV SI, OFFSET num     ; Load address of num into SI
    MOV DI, OFFSET ones_count ; Load address of ones_count array into DI
    MOV CX, 10                ; Loop counter for 10 values

COUNT_ONES:
    ; Load current value from values array into AL
    MOV AL, BYTE PTR [SI]

    ; Initialize count of 1s to 0
    XOR BX, BX                ; CLEAR BX,BX will hold the count of 1s
    MOV CH, 4                 ; max num in array is 1001, 4 bit is needed 

COUNT_BITS:
    SHR AL, 1                 ; Shift right to bring the least significant bit to the carry flag
    JNC SKIP_INCREMENT        ; If no carry (bit was 0), skip increment
    INC BX                    ; Increment BX (count of 1s)

SKIP_INCREMENT:
    DEC CH                    ; Decrement bit counter
    JNZ COUNT_BITS            ; Repeat until all bits are processed

    ; Store the count of 1s in the ones_count array
    MOV BYTE PTR[DI], BL

    ; Move to the next value,it is byte so 1 inc is enough
    INC SI

    ; Move to the next position,it is byte so 1 inc is enough
    INC DI
    
    ; Decrement loop counter and repeat for next value
    LOOP COUNT_ONES

    INT 20h                   

CODE ENDS
END START