# Architecture Specification

## Overview
CHM Cambodia DNS Server provides an intelligent DNS routing layer that combines:
1. Fast local edge caching using Unbound/CoreDNS.
2. Encrypted DoH/DoT upstream forwarding.
3. Geo-optimized routing for Cambodia telecommunications.
