class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        min_energy = sum(task[0] for task in tasks)
        init_energy = min_energy

        sorted_tasks = sorted(tasks, key=lambda item:item[1] - item[0], reverse=True)

        for task in sorted_tasks:
            if min_energy >= task[1]:
                min_energy -= task[0]
            else:
                min_energy = task[1] - task[0]
        
        return init_energy + min_energy