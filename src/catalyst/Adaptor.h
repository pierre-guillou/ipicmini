#ifndef FEADAPTOR_HEADER
#define FEADAPTOR_HEADER

#include <vector>

namespace Adaptor
{
void Initialize(char* script);

void Finalize();

void CoProcess(
  const std::vector<double>& pos, const std::vector<double>& velocity, const std::vector<int>& collisions, double time, unsigned int timeStep);
}

#endif
