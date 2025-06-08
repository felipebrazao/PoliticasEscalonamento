import time
import random
from collections import deque
import sys
import curses

def create_process(pid, name, burst_time, priority=0):
    return {
        "pid": pid,
        "name": name,
        "total_burst": burst_time,
        "remaining_burst": burst_time,
        "priority": priority,
        "progress": 0,
        "finished": False
    }

def execute_process(process, quantum):
    if process["remaining_burst"] <= quantum:
        executed = process["remaining_burst"]
        process["remaining_burst"] = 0
        process["finished"] = True
    else:
        executed = quantum
        process["remaining_burst"] -= quantum
    
    process["progress"] = ((process["total_burst"] - process["remaining_burst"]) / process["total_burst"]) * 100
    return executed

def run_fifo(processes, stdscr):
    time = 0
    completed = []
    queue = deque(processes.copy())
    
    while queue:
        current = queue.popleft()
        while not current["finished"]:
            execute_process(current, 1)
            time += 1
            display_processes(processes, time, "FIFO", stdscr)
            time.sleep(0.1)
        completed.append(current)
    
    return completed

def run_rr(processes, quantum, stdscr):
    time = 0
    completed = []
    queue = deque(processes.copy())
    
    while queue:
        current = queue.popleft()
        executed = execute_process(current, quantum)
        time += executed
        
        if current["finished"]:
            completed.append(current)
        else:
            queue.append(current)
        
        display_processes(processes, time, "RR", stdscr)
        time.sleep(0.1)
    
    return completed

def run_priority(processes, stdscr):
    priority_queue = sorted(processes, key=lambda x: x["priority"])
    return run_fifo(priority_queue, stdscr)


def display_processes(processes, current_time, algorithm, stdscr):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    
    title = f"Corrida de Processos - {algorithm} - Tempo: {current_time}"
    stdscr.addstr(0, (width - len(title)) // 2, title)
    
    for i, process in enumerate(processes):
        progress_bar_length = width - 30
        filled = int(process["progress"] * progress_bar_length / 100)
        bar = '█' * filled + '-' * (progress_bar_length - filled)
        
        status = "COMPLETO!" if process["finished"] else f"Executando... ({process['remaining_burst']}ms restantes)"
        priority_info = f" [Prioridade: {process['priority']}]" if algorithm == "PRIORITY" else ""
        
        info_line = f"{process['name']} (PID: {process['pid']}){priority_info}: {status}"
        stdscr.addstr(2 + i*2, 0, info_line)
        stdscr.addstr(3 + i*2, 0, f"[{bar}] {process['progress']:.1f}%")
    
    stdscr.refresh()

def show_results(completed_processes, stdscr):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    
    if completed_processes:
        winner = completed_processes[0]
        message = f"Vencedor: {winner['name']} (PID: {winner['pid']})!"
        stdscr.addstr(height//2 - 1, (width - len(message)) // 2, message)
    
    stdscr.addstr(height//2 + 1, (width - 20) // 2, "Pressione qualquer tecla para sair...")
    stdscr.refresh()
    stdscr.getch()


def create_processes(num_processes, algorithm):
    names = ["Explorador", "Calculador", "Navegador", "Gerenciador", "Monitor"]
    icons = ["🚀", "🧮", "🌐", "🛠️", "👁️"]
    processes = []
    
    for i in range(num_processes):
        name = f"{icons[i]} {names[i]}"
        burst = random.randint(5, 20)
        priority = random.randint(1, 5) if algorithm == "PRIORITY" else 0
        processes.append(create_process(i+1, name, burst, priority))
    
    return processes


def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    
    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        
        title = "CORRIDA DE PROCESSOS - SIMULADOR DE ESCALONAMENTO"
        stdscr.addstr(1, (width - len(title)) // 2, title)
        
        menu = [
            "Escolha o algoritmo de escalonamento:",
            "1. FIFO (First In, First Out)",
            "2. Round Robin (Quantum = 3)",
            "3. Por Prioridade",
            "4. Sair"
        ]
        
        for i, line in enumerate(menu):
            stdscr.addstr(3 + i, (width - len(line)) // 2, line)
        
        stdscr.refresh()
        
        key = stdscr.getch()
        if key == ord('1'):
            algorithm = "FIFO"
        elif key == ord('2'):
            algorithm = "RR"
        elif key == ord('3'):
            algorithm = "PRIORITY"
        elif key == ord('4'):
            break
        else:
            continue
        
        num_processes = random.randint(3, 5)
        processes = create_processes(num_processes, algorithm)
        quantum = 3 if algorithm == "RR" else 1
        
        if algorithm == "FIFO":
            completed = run_fifo(processes, stdscr)
        elif algorithm == "RR":
            completed = run_rr(processes, quantum, stdscr)
        elif algorithm == "PRIORITY":
            completed = run_priority(processes, stdscr)
        
        show_results(completed, stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
    print("Obrigado por jogar a Corrida de Processos!")