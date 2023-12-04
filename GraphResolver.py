import networkx

def Creategraph():
    xone = "XONE"
    red = "RED"
    riskone = "RiskONE"
    effcom = "Effcom"
    rdws = "RDWS"
    orchestrator = "Orchestrator"
    sgdocs = "SGDocs"
    pricingview = "PricingView"
    kidwebsite = "KidWebsite"
    graph = networkx.DiGraph()
    graph.add_edges_from([(effcom, xone), (xone, orchestrator), (red, orchestrator), (riskone, orchestrator), (rdws, riskone), (pricingview, riskone), (orchestrator, kidwebsite), (orchestrator, sgdocs)])
    return graph

def GetImpactedApplications(source):
    graph = Creategraph()
    return networkx.descendants(graph, source)