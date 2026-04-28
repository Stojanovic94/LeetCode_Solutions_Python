class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], 
                                allowedSwaps: List[List[int]]) -> int:
        n = len(source)

        # Special case check for no swaps allowed.
        # 8 of 71 test cases.  (11%)  Apr 2026
        if len(allowedSwaps) == 0:
            hamDist = 0
            for i in range(n):
                if source[i] != target[i]:
                    hamDist += 1
            return hamDist

        # Routine for "find" part of union-find.
        def find(u: int) -> int:
            nonlocal parents
            if parents[u] == u:  return u
            parents[u] = find(parents[u])
            return parents[u]

        # Group the array indexes by indexes interconnected through their 
        # allowed swaps, using a union-find.
        parents = list(range(n))
        groupSize = [1] * n
        allConnected = False
        for u,v in allowedSwaps:
            uPar = find(u)
            vPar = find(v)
            if uPar != vPar:
                parents[uPar] = vPar
                groupSize[vPar] += groupSize[uPar]
                if groupSize[vPar] == n:
                    allConnected = True
                    break

        # Convert members of each union-find group to a list of values 
        # from the source[] array, and a list of values from the target 
        # array.  A pair of lists for each group.
        hamDist = 0
        valsInGroup = defaultdict(list)
        targetsInGroup = defaultdict(list)
        if allConnected:
            # One group only, because all n values are connected by swaps.
            # 40 of 71 test cases.  (56%)  Apr 2026
            valsInGroup[0] = source
            targetsInGroup[0] = target
        else:
            # Multiple groups.
            for u in range(n):
                uPar = find(u)
                if groupSize[uPar] == 1:
                    if source[u] != target[u]:
                        hamDist += 1
                else:
                    valsInGroup[uPar].append(source[u])
                    targetsInGroup[uPar].append(target[u])
        
        # Find hamming distance for each group's pair of lists.  One list 
        # of the pair being the source values for the group, and the other 
        # list being the target values for the group.  Sort the two lists 
        # to be able to find how many list elements are different between 
        # the two lists.  This method handles duplicates within each list.
        for u, srcList in valsInGroup.items():
            tLen = len(srcList)
            tarList = targetsInGroup[u]
            srcList.sort()
            tarList.sort()
            tIdx = 0
            # For each value in source list, try to find a matching value 
            # in target list.  Since both lists are sorted in ascending 
            # order, both lists can be processed sequentially.  Using a 
            # Python Counter to do this is much simpler but slower code.
            for s in srcList:
                if tarList[tIdx] < s:
                    while tIdx < tLen and tarList[tIdx] < s:
                        hamDist += 1
                        tIdx += 1
                    if tIdx >= tLen:  break
                if tarList[tIdx] == s:
                    tIdx += 1
                    if tIdx >= tLen:  break
            hamDist += tLen - tIdx
        
        return hamDist


# -----------------------------------------------------------
# class Solution:
#     def minimumHammingDistance(self, source: List[int], target: List[int], 
#                                 allowedSwaps: List[List[int]]) -> int:
#         n = len(source)

#         # Special case check for no swaps allowed.
#         # 8 of 71 test cases.  (11%)  Apr 2026
#         if len(allowedSwaps) == 0:
#             hamDist = 0
#             for i in range(n):
#                 if source[i] != target[i]:
#                     hamDist += 1
#             return hamDist

#         # Routine for "find" part of union-find.
#         def find(u: int) -> int:
#             nonlocal parents
#             if parents[u] == u:  return u
#             parents[u] = find(parents[u])
#             return parents[u]

#         # Group the array indexes by indexes interconnected through their 
#         # allowed swaps, using a union-find.
#         parents = list(range(n))
#         for u,v in allowedSwaps:
#             uPar = find(u)
#             vPar = find(v)
#             if uPar != vPar:
#                 parents[vPar] = uPar

#         # Convert members of each union-find group to a list of values 
#         # from the source[] array, and a list of values from the target 
#         # array.  A pair of lists for each group.
#         valsInGroup = defaultdict(list)
#         targetsInGroup = defaultdict(list)
#         for u in range(n):
#             uPar = find(u)
#             valsInGroup[uPar].append(source[u])
#             targetsInGroup[uPar].append(target[u])
        
#         # Find hamming distance for each group's pair of lists.  One list 
#         # of the pair being the source values for the group, and the other 
#         # list being the target values for the group.  Sort the two lists 
#         # to be able to find how many list elements are different between 
#         # the two lists.  This method handles duplicates within each list.
#         hamDist = 0
#         for u, srcList in valsInGroup.items():
#             tLen = len(srcList)
#             # If lists only have one value, then this special case is an 
#             # easy test.
#             if tLen == 1:
#                 if srcList[0] != targetsInGroup[u][0]:
#                     hamDist += 1
#                 continue
#             tarList = targetsInGroup[u]
#             srcList.sort()
#             tarList.sort()
#             tIdx = 0
#             # For each value in source list, try to find a matching value 
#             # in target list.  Since both lists are sorted in ascending 
#             # order, both lists can be processed sequentially.  Using a 
#             # Python Counter to do this is much simpler but slower code.
#             for s in srcList:
#                 if tarList[tIdx] < s:
#                     while tIdx < tLen and tarList[tIdx] < s:
#                         hamDist += 1
#                         tIdx += 1
#                     if tIdx >= tLen:  break
#                 if tarList[tIdx] == s:
#                     tIdx += 1
#                     if tIdx >= tLen:  break
#             hamDist += tLen - tIdx
        
#         return hamDist


# -----------------------------------------------------------
# class Solution:
#     def minimumHammingDistance(self, source: List[int], target: List[int], 
#                                 allowedSwaps: List[List[int]]) -> int:
#         n = len(source)

#         # "Find" part of union-find.
#         def find(u: int) -> int:
#             nonlocal parents
#             if parents[u] == u:  return u
#             parents[u] = find(parents[u])
#             return parents[u]

#         # Group the array indexes by indexes interconnected through their 
#         # allowed swaps, using a union-find.
#         parents = list(range(n))
#         for u,v in allowedSwaps:
#             uPar = find(u)
#             vPar = find(v)
#             if uPar != vPar:
#                 parents[vPar] = uPar

#         # Convert members of each union-find group to a list of values 
#         # from the source[] array, and a list of values from the target 
#         # array.  A pair of lists for each group.
#         valsInGroup = defaultdict(list)
#         targetsInGroup = defaultdict(list)
#         for u in range(n):
#             uPar = find(u)
#             valsInGroup[uPar].append(source[u])
#             targetsInGroup[uPar].append(target[u])
        
#         # Find hamming distance for each group's pair of lists.  One list 
#         # of the pair being the source values for the group, and the other 
#         # list being the target values for the group.  Sort the two lists 
#         # to be able to find how many list elements are different between 
#         # the two lists.  This method handles duplicates within each list.
#         hamDist = 0
#         for u, srcList in valsInGroup.items():
#             tarList = targetsInGroup[u]
#             tLen = len(tarList)
#             if tLen > 1:
#                 srcList.sort()
#                 tarList.sort()
#             tIdx = 0
#             # For each value in source list, try to find a matching value 
#             # in target list.  Since both lists are sorted in ascending 
#             # order, both lists can be processed sequentially.  Using a 
#             # Python Counter to do this is much simpler but slower code.
#             for s in srcList:
#                 if tarList[tIdx] < s:
#                     while tIdx < tLen and tarList[tIdx] < s:
#                         hamDist += 1
#                         tIdx += 1
#                     if tIdx >= tLen:  break
#                 if tarList[tIdx] == s:
#                     tIdx += 1
#                     if tIdx >= tLen:  break
#             hamDist += tLen - tIdx
        
#         return hamDist


# -----------------------------------------------------------
# # More complex code, but faster than code farther below.
# class Solution:
#     def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
#         n = len(source)

#         def find(u: int) -> int:
#             nonlocal parents
#             if parents[u] == u:  return u
#             parents[u] = find(parents[u])
#             return parents[u]

#         parents = list(range(n))
#         for u,v in allowedSwaps:
#             uPar = find(u)
#             vPar = find(v)
#             if uPar != vPar:
#                 parents[vPar] = uPar
#         for u in range(n):  find(u)

#         valsInGroup = defaultdict(list)
#         targetsInGroup = defaultdict(list)
#         for u, uPar in enumerate(parents):
#             valsInGroup[uPar].append(source[u])
#             targetsInGroup[uPar].append(target[u])
        
#         hamDist = 0
#         for u, srcList in valsInGroup.items():
#             counts = defaultdict(int)
#             for val in srcList:
#                 counts[val] += 1
#             for val in targetsInGroup[u]:
#                 counts[val] -= 1
#             hamDist += sum((cnt for cnt in counts.values() if cnt > 0), 0)
        
#         return hamDist


#----------------------------------------------------------------
# # Simpler code, but slower.
# class Solution:
#     def minimumHammingDistance(self, source: List[int], target: List[int], 
#                                 allowedSwaps: List[List[int]]) -> int:
#         n = len(source)

#         def find(u: int) -> int:
#             nonlocal parents
#             if parents[u] == u:  return u
#             parents[u] = find(parents[u])
#             return parents[u]

#         parents = list(range(n))
#         for u,v in allowedSwaps:
#             uPar = find(u)
#             vPar = find(v)
#             if uPar != vPar:
#                 parents[vPar] = uPar

#         valsInGroup = defaultdict(list)
#         targetsInGroup = defaultdict(list)
#         for u in range(n):
#             uPar = find(u)
#             valsInGroup[uPar].append(source[u])
#             targetsInGroup[uPar].append(target[u])
        
#         hamDist = 0
#         for u in valsInGroup.keys():
#             hamDist += sum((Counter(valsInGroup[u]) - 
#                         Counter(targetsInGroup[u])).values(), 0)
        
#         return hamDist