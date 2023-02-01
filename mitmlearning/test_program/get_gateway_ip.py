def get_default_gateway(self):
        for r in getattr(self, 'routes', []):
            if r.get('subnet', '') == '0.0.0.0/0':
                return r.get('gateway', None)

        return None
    
get_default_gateway(self)