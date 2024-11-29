import time
import functools
import logging
from fastapi import Request
from typing import Callable, Any


def monitor_latency(logger=logging.getLogger()):
    def decorator(func: Callable):
        @functools.wraps(func)
        async def wrapper(*args: Any, **kwargs: Any):
            # Verifica se há request como primeiro argumento
            request = next(
                (arg for arg in args if isinstance(arg, Request)), None)

            start_time = time.time()
            try:
                result = await func(*args, **kwargs)

                # Calcula latência
                latency = time.time() - start_time

                # Log de latência
                if request:
                    # Se for uma request do FastAPI, adiciona detalhes
                    logger.info(f"Rota: {request.url.path} | "
                                f"Método: {request.method} | "
                                f"Latência: {latency:.4f} segundos")
                else:
                    # Log genérico se não for request
                    logger.info(
                        f"Latência da função {func.__name__}: {latency:.4f} segundos")

                return result

            except Exception as e:
                latency = time.time() - start_time
                logger.error(f"Erro na função {func.__name__}: "
                             f"Latência {latency:.4f} segundos | Erro: {e}")
                raise
        return wrapper
    return decorator
