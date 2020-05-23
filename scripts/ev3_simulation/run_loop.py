import time
import multiprocessing
import asyncio
import logging


LOOP_TIME = 1/120

class RunLoop:
    def __init__(self):
        self.process = multiprocessing.Process(target=self.__bootstrap_loop_process)
        self.logger = logging.getLogger("ev3.simulation_engine")
        self.logger.setLevel(logging.INFO)
        pass

    def start_simulation(self):
        if not self.process.is_alive():
            self.process.start()

    def stop_simulation(self):
        if self.process.is_alive():
            self.process.terminate()
            self.process = multiprocessing.Process(target=self.__bootstrap_loop_process)

    def __bootstrap_loop_process(self):
        self.logger.info('ENGINE PROCESS: Setting up event loop')
        asyncio.run(self.__run_engine_loop())

    async def __run_engine_loop(self):
        loop = asyncio.get_event_loop()
        start_time = loop.time()
        current_time = start_time
        last_loop_time = start_time

        while True:
            current_time = loop.time()
            elapsed_time = current_time - last_loop_time
            self.logger.warning('ENGINE PROCESS: Running engine -- loop_time: %0.0d, total_time: %0.0d', elapsed_time*1000, (current_time - start_time)*1000)
            # print(f'Running engine -- loop time: {round(elapsed_time*1000)}, total_time: {round((current_time - start_time)*1000)}')
            last_loop_time = current_time
            await asyncio.sleep(LOOP_TIME)


if __name__ == "__main__": 
    run_loop = RunLoop()
    run_loop.start_simulation()
    time.sleep(5)
    run_loop.stop_simulation()
    run_loop.start_simulation()
    run_loop.start_simulation()
    time.sleep(3)
    run_loop.stop_simulation()
    run_loop.stop_simulation()
    print('ENGINE PROCESS: Done')