import asyncio
import httpx

class Autoreg:
    def __init__(self, app, log=None, settings):
         """[Auto registration endpoints in DAC]
        Args:
            app: [Instance of Fastapi app]
            log: Optional: [Instance of Log]
            settings: [Instance of Settings]
        """
        self.app = app
        self.log = log
        # endpoints in exclude_list is not registered in DAC
        self.exclude_list = ["/openapi.json", "/docs", "/docs/oauth2-redirect", "/redoc", "/metrics/"]
        self.dac_uri = settings.DAC_URI 
        self.service_name = settings.service_name
        self.prefixes = set()

    async def autoreg():
        """
        [autoreg function creates service and endpoints]
        """

        # Gettings routes from app instance and creating prefixes set
        for route in self.app.routes:
            if route.path not in self.exclude_list:
                try:
                    self.prefixes.add(route.path)
                except Exception as err:
                    if self.log:
                        self.log.error(err, exc_info=True)
                    else:
                        print("prefix error -> ", err)

        # Creating service
        service_id = await self.create_service(service_name)

        # If service created successfully, creating endpoints with foreign key to this service: self.service_name
        if service_id:
            await create_endpoints(service_id)


    async def create_endpoints(service_id: str):
        """[summary]

        Args:
            service_id (str): [service_id of created service]
        [Creating endpoints pointing to service_id]
        """
        for prefix in self.prefixes:
            async with httpx.AsyncClient() as client:
                await client.post(
                    f"{self.dac_uri}/endpoints", 
                    json={"service_id": service_id, "prefix": prefix}
                    )
                
                # If log instance then log info else print
                if self.log:
                    self.log.info(f"{prefix} created")
                else:
                    print(f"{prefix} created")


    async def create_service(service_name: str):
        """[summary]

        Args:
            service_name (str): [service_name taken from settings.SERVICE_NAME]

        Returns:
            [type]: [service id]
        
        Flow:
            [get service_id] if exists return service_id
            [create service_id] if service not exists
        """
        # In one async with client we can not send 2 requests. 

        # Get service_name from database. Return id if exists
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{dac_uri}/services/by-name/{service_name}")
            if response.status_code == HTTPStatus.OK:
                if self.log:
                    self.log.info(f"{response.json().get('name')} exists")
                else:
                    print(f"{response.json().get('name')} exists")
                return response.json().get("id")
        
        # Create service_name if not exists
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{dac_uri}/services", json = {"name": service_name})

            # If log instance then log info else print
            if self.log:
                self.log.info(f"{response.json().get('name')} created")
            else:
                print(f"{response.json().get('name')} created")

            if response:
                return response.json().get("id")