class WeatherService:

    def __init__(self):
        self.name = 'Polyanna'
        self.current_snow_fall_rate = 0


    async def initializer(self):
        logger.info('Service weather initializing')
        while True:
            await sleep(1)
        
        async def get_current_snow_fall_rate(self):
            return self.current_snow_fall_rate