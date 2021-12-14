## 2. Matrix Vector Multiplication ##

matrix_a = np.asarray([
    [0.7,3,9],
    [1.7,2,9],
    [0.7,9,2]
], dtype=np.float32)

matrix_b = np.asarray([
    [1],
    [2],
    [1]
], dtype=np.float32)

ab_product=np.dot(matrix_a,matrix_b)

## 3. Matrix Multiplication ##

matrix_a = np.asarray([
    [0.7, 3],
    [1.7, 2],
    [0.7, 9]
], dtype=np.float32)

matrix_b = np.asarray([
    [113, 3, 10],
    [1, 0, 1],
], dtype=np.float32)


product_ab=np.dot(matrix_a,matrix_b)

product_ba=np.dot(matrix_b,matrix_a)

## 4. Matrix Transpose ##

matrix_a = np.asarray([
    [0.7, 3],
    [1.7, 2],
    [0.7, 9]
], dtype=np.float32)

matrix_b = np.asarray([
    [113, 3, 10],
    [1, 0, 1],
], dtype=np.float32)

transpose_a=np.transpose(matrix_a)
transpose_b=np.transpose(matrix_b)
print(transpose_a)

trans_ba=np.dot(transpose_b,transpose_a)
trans_ab=np.dot(transpose_a,transpose_b)

product_ab=np.dot(matrix_a,matrix_b)

print(trans_ba==np.transpose(product_ab))

## 5. Identity Matrix ##

i_2 = np.asarray([
    [1, 0],
    [0, 1]
], dtype=np.float32)
i_3 = np.asarray([
    [1, 0,0],
    [0, 1,0],
    [0, 0,1]
], dtype=np.float32)

matrix_33=np.asarray([
    [2, 0,0],
    [0, 2,0],
    [0, 0,2]
], dtype=np.float32)

matrix_23=np.asarray([
    [2, 0,0],
    [0, 2,0]], dtype=np.float32)


identity_33=np.dot(matrix_33,i_3)

identity_23=np.dot(np.transpose(matrix_23),i_2)

## 6. Matrix Inverse ##

matrix_a = np.asarray([
    [1.5, 3],
    [1, 4]
])

def matrix_inverse_two(mat):
    cal=mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
    try:
        if(cal==0):
            raise
            
        else:
            m = np.asarray([
            [0.0, 0.0],
            [0.0, 0.0]
            ])
            print(mat)
            m[0][0]=mat[1][1]
            m[1][1]=mat[0][0]
            m[0][1]=-1*mat[0][1]
            m[1][0]=-1*mat[1][0]
            print(m)

            return m/cal
    except:
            print("nt possible")
            raise
    
    
inverse_a=matrix_inverse_two(matrix_a)

i_2=np.dot(matrix_a,inverse_a)
print(i_2)
        

## 7. Solving The Matrix Equation ##

matrix_a = np.asarray([
    [30, -1],
    [50, -1]
])

def matrix_inverse_two(mat):
    cal=mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
    try:
        if(cal==0):
            raise
            
        else:
            m = np.asarray([
            [0.0, 0.0],
            [0.0, 0.0]
            ])
            print(mat)
            m[0][0]=mat[1][1]
            m[1][1]=mat[0][0]
            m[0][1]=-1*mat[0][1]
            m[1][0]=-1*mat[1][0]
            print(m)

            return m/cal
    except:
            print("nt possible")
            raise
            
solution_x=np.dot(matrix_inverse_two(matrix_a),np.asarray([
    [-1000],
    [-100]
]))

solution_x=np.dot(np.linalg.inv(matrix_a),np.asarray([
    [-1000],
    [-100]
]))

## 8. Determinant For Higher Dimensions ##

matrix_22 = np.asarray([
    [8, 4],
    [4, 2]
])

matrix_33 = np.asarray([
    [1, 1, 1],
    [1, 1, 6],
    [7, 8, 9]
])

det_22=np.linalg.det(matrix_22)
det_33=np.linalg.det(matrix_33)