import numpy as np

# 1. 余弦相似度
def cosine_similarity_custom(A, B):
    dot_product = np.dot(A, B)
    norm_A = np.linalg.norm(A)
    norm_B = np.linalg.norm(B)
    return dot_product / (norm_A * norm_B)

# 2. 欧氏距离
def euclidean_distance_custom(A, B):
    return np.linalg.norm(A - B)

# 3. 曼哈顿距离
def manhattan_distance_custom(A, B):
    return np.sum(np.abs(A - B))

# 4. 皮尔逊相关系数
def pearson_correlation_custom(A, B):
    return np.corrcoef(A, B)[0, 1]

# 5. 杰卡德相似度
def jaccard_similarity_custom(A, B):
    intersection = len(set(A) & set(B))
    union = len(set(A) | set(B))
    return intersection / union

# 6. 点积
def dot_product_custom(A, B):
    return np.dot(A, B)


if __name__ == '__main__':
    # 示例数据
    A = np.array([1, 2, 3])
    B = np.array([4, 5, 6])

    # 计算并输出结果
    print("余弦相似度 (自定义):", cosine_similarity_custom(A, B))

    print("欧氏距离 (自定义):", euclidean_distance_custom(A, B))

    print("曼哈顿距离:", manhattan_distance_custom(A, B))

    print("皮尔逊相关系数:", pearson_correlation_custom(A, B))

    A_list = [1, 2, 3]
    B_list = [2, 3, 4]
    print("杰卡德相似度:", jaccard_similarity_custom(A_list, B_list))

    print("点积:", dot_product_custom(A, B))